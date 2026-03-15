import psycopg2
from contextlib import contextmanager

"""
    Human written code finetuned to my database.
    Tested for all KPIs.
"""

#Variable definitions [to be moved to .env file later]
DB_NAME = "video_db"
DB_USER = "postgres"
DB_PASSWORD = "%40Sri939897"
#Dict that maps columns to their tables
COLUMN_MAP ={
    "User": "channel_and_user",
    "Input Type": "input_type",
    "Language": "language",
    "Month": "month_wise_duration",
    "Output Type": "output_type",
    "Reels":"channel_wise_publishing",
    "Facebook":"channel_wise_publishing",
    "Instagram":"channel_wise_publishing",
    "Linkedin":"channel_wise_publishing",
    "Reels":"channel_wise_publishing",
    "Shorts":"channel_wise_publishing",
    "X":"channel_wise_publishing",
    "Youtube":"channel_wise_publishing",
    "Threads":"channel_wise_publishing",
    "Reels Duration":"channel_wise_publishing_duration",
    "Facebook Duration":"channel_wise_publishing_duration",
    "Instagram Duration":"channel_wise_publishing_duration",
    "Linkedin Duration":"channel_wise_publishing_duration",
    "Reels Duration":"channel_wise_publishing_duration",
    "Shorts Duration":"channel_wise_publishing_duration",
    "X Duration": "channel_wise_publishing_duration",
    "Youtube Duration": "channel_wise_publishing_duration",
    "Threads Duration": "channel_wise_publishing_duration"
}

COMMON_COLUMNS = ["Uploaded Count",
    "Created Count",
    "Published Count",
    "Uploaded Duration (hh:mm:ss)",
    "Created Duration (hh:mm:ss)",
    "Published Duration (hh:mm:ss)",
    "Channel"]

@contextmanager
def get_connection():
    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password= DB_PASSWORD,
        host="localhost",
    )
    try:
        yield conn
    finally:
        conn.close()

def get_data(
        columns = [],
        aggs = None,
        agg_columns = [],
        filters = None,
        group_by = [],
        sort_col = [],
        order = "ASC",
        limit = 10,
        offset = 0
):
    
    query = "SELECT "
    tables = []

    if columns:
        if not isinstance(columns, list):
            columns = [columns]
        query += ','.join([f"\"{column}\"" for column in columns])
        


    if aggs:
        if columns:
            query += " ,"
        aggregates = [f"{agg.upper()}(\"{agg_columns[i]}\")" for i, agg in enumerate(aggs)]
        query += ",".join(aggregates)
        

    all_relevant_columns = []
    all_relevant_columns.extend(columns)
    all_relevant_columns.extend(agg_columns)
    if filters:
        filter_cols = [f["column"] for f in filters]
        all_relevant_columns.extend(filter_cols)
    tables = list(set([COLUMN_MAP[col] for col in all_relevant_columns if col not in COMMON_COLUMNS]))

    if len(tables) == 0:
        tables = ["channel_and_user"]


    if len(tables) != 1:
        print(f"No. of tables found to be differnet from 1. Tables: {len(tables)}")

    query += " "
    query += f"FROM \"{tables[0]}\""

    if filters:
        conditions = []

        for f in filters:

            column = f["column"]
            op = f.get("op", "=")
            value = f["value"]

            if op.upper() == "IN":
                col_vals = ", ".join([f"\'{val}\'" for val in value])
                conditions.append(f"\"{column}\" IN ({col_vals})")

            else:
                conditions.append(f"\"{column}\" {op} \'{value}\'")

        query += " WHERE " + " AND ".join(conditions)


    if group_by:
        if not isinstance(group_by, list):
            group_by = [group_by]
        query += " GROUP BY " + " GROUP BY ".join([f"\"{col}\"" for col in group_by])

    if columns and aggs:
        if not group_by:
            query += " GROUP BY "
        else:
            query += " ,"
        query += ", ".join([f"\"{col}\"" for col in columns])

    if sort_col:
        if sort_col.startswith(("SUM", "COUNT", "AVG")):
            query += " ORDER BY " + f"{sort_col} " + f"{order.upper()}"
        else:
            query += " ORDER BY " + f"\"{sort_col}\" " + f"{order.upper()}"

    query += f" LIMIT {limit}"
    query += f" OFFSET {offset}"
    query += ";"


    print(query)
    with get_connection() as conn:
        curr = conn.cursor()
        curr.execute(query)
        result = curr.fetchall()
        curr.close()
    print(f"\n\n{result}")



filters = [
    {
        "column": "Output Type",
        "op": "=",
        "value": "Chapters"
    }
]
get_data(columns= ["Reels", "Channel"],limit= 100)    # explain what happening how to analyse it and how to run it 
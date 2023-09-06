from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    import sqlite3
    con = sqlite3.connect('erp.db')

    cur = con.cursor()

    # Create table
    cur.execute('''CREATE TABLE IF NOT EXISTS 教師
        (姓名 text, 郵件 text, 研究室 integer)''')

    # Insert a row of data
    cur.execute("INSERT INTO 教師 VALUES ('楊子青','tcyang@pu.edu.tw', 579)")
    cur.execute("INSERT INTO 教師 VALUES ('王耀德','ytwang@pu.edu.tw', 686)")
    cur.execute("INSERT INTO 教師 VALUES ('陳武林','wlchen@pu.edu.tw', 665)")

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()
    return "erp.db has created"

#if __name__ == "__main__":
#    app.run()
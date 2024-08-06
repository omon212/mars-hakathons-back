import sqlite3

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()


def referal_code(invite_code, message_id):
    select_user_id = cursor.execute("SELECT id FROM Calculator_homemodel WHERE id = ?", (invite_code,)).fetchone()
    inviter_user_id = ""
    for i in select_user_id:
        inviter_user_id += str(i)

    print(inviter_user_id)
    if inviter_user_id:
        try:
            cursor.execute("UPDATE Calculator_homemodel SET connected_telegram = ? WHERE id = ?",
                           (message_id, inviter_user_id))
            conn.commit()
            # print("Update successful.")
            return 'Sucsess'
        except sqlite3.Error as e:
            return 'Error'
            # print(f"An error occurred: {e}")

import psycopg2
from classes.connection_files import host, user, password, db_name

try:
    conn=psycopg2.connect(host=host, user=user, password=password, database=db_name)
    conn.autocommit=True

except (Exception, psycopg2.Error) as _ex:
    print(f'Can`t establish connection to database{_ex}')

def auth_stud(nick, password):
    with conn.cursor() as cursor:
        ''' Проверяем, есть в базе данных переданные строки.'''

        cursor.execute(f"""SELECT "Nick", "Email"
    FROM public."User"
    where "Nick" = '{nick}' and "Password" = '{password}'; """)
        result = cursor.fetchall()
    if result:
        return result[0]
    else:
        return False

def reg_stud(nick, password, email):
    with conn.cursor() as cursor:
        cursor.execute("""SELECT MAX("ID_user") FROM public."User" """)
        result = cursor.fetchone()
        current_ID_user = result[0]
        new_ID_user = current_ID_user + 1 if current_ID_user is not None else 1

        # Проверка на уникальность значений
        cursor.execute("""SELECT "Nick", "Email", "Password" FROM public."User" WHERE "Nick"=%s OR "Email"=%s OR "Password"=%s""",
                       (nick, email, password))
        duplicates = cursor.fetchall()
        if duplicates:
            print("Ошибка: данные не могут быть добавлены, так как некоторые значения уже существуют.")
            return

        # Вставка данных
        cursor.execute("""INSERT INTO public."User" ("ID_user", "Nick", "Email", "Password") VALUES (%s, %s, %s, %s)""",
                       (new_ID_user, nick, email, password))

        if result:
            return result[0]

        else:
            return False

def got_items():
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "ID_ref.material"
	FROM public."ref.material";""")
        res = cursor.fetchall()
    return res

def got_prac_items():
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "ID_practice" FROM public."practice"; """)
        res = cursor.fetchall()
    return res

def got_head(id):
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "Heading"
	FROM public."ref.material"
	where "ID_ref.material" = %s """, (id))
        res_mas = cursor.fetchall()
    return res_mas

def got_content(id):
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "Content"
	FROM public."ref.material"
	where "ID_ref.material" = %s """, (id))
        res_mas = cursor.fetchall()
    return res_mas

def got_conclusion(id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("""SELECT "Conclusion"
            FROM public."ref.material"
            where "ID_ref.material" = %s """, (id))
            res_mas = cursor.fetchall()
        return res_mas
    except (psycopg2.Error) as error:
        print(error)

def got_tree_id():
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "ID_test" from public."tests"
        ORDER BY "ID_test" """)
        res_items = cursor.fetchall()
    return res_items

def get_task_index(name):

    with conn.cursor() as cursor:
        cursor.execute(f"""SELECT "id_test" from public."task"
                        Where "Task" = '{name}'""")

        res_items = cursor.fetchall()

    res_items = res_items[0]
    return res_items[0] - 1

def got_tree_tests():

    with conn.cursor() as cursor:
        cursor.execute("""SELECT "Name" from public."tests" """)
        res_items = cursor.fetchall()

    _tests = []

    for i in res_items:
        for j in i:
            _tests.append(str(j))

    return _tests

def got_tree_tasks():

    with conn.cursor() as cursor:
        cursor.execute("""SELECT "Task"
	FROM public.task; """)
        res_tasks = cursor.fetchall()

    _tasks = []

    for i in res_tasks:
        for j in i:
            _tasks.append(str(j))

    return _tasks

def got_tree_id():
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "id_test" from public."task" """)
        res_id = cursor.fetchall()

    _id = []

    for i in res_id:
        for j in i:
            _id.append(int(j))

    _id.sort()

    return _id

def maneg_regis(name, last_name, patronymic, date_of_birth, key, password):
    with conn.cursor() as cursor:
        try:
            # Проверяем, есть ли key в таблице keys
            cursor.execute(""" SELECT id_key
	FROM public.keys WHERE key = %s """, (key,))
            key_id = cursor.fetchone()

            if key_id is not None:
                key_id = key_id[0]

                # Проверяем, отсутствует ли внешний ключ элемента key в таблице managers
                cursor.execute("""SELECT id_key FROM public."managers" WHERE id_key = %s""", (key_id,))
                manager_id = cursor.fetchone()

                if manager_id is None:
                    # Получаем ID_man предыдущей записи
                    cursor.execute(""" SELECT MAX("ID_man.") FROM public."managers" """)
                    previous_id = cursor.fetchone()[0] or 0

                    # Генерируем новый ID_man для новой записи
                    new_id = previous_id + 1

                    # Записываем данные в таблицу managers
                    cursor.execute(
                        """INSERT INTO public."managers" ("ID_man.", "surname", "name", "patronymic", "date_of_birth", "id_key", "password") VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                        (new_id, name, last_name, patronymic, date_of_birth, key_id, password))

                    # Подтверждаем изменения в базе данных
                    #conn.commit()

                    print( "Данные успешно добавлены")
                    return True
                else:
                    print("Указанный key уже связан с записью в таблице managers")
                    return False
            else:
                return False
                print ("Указанный key не найден в таблице keys")

        except (Exception, psycopg2.Error) as error:
            conn.rollback()
            print(str(error))
            return False

def maneg_auth(name, last_name, password):
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "name", "surname", "password" 
        from public."managers" where "name" = %s and "surname" = %s and "password" = %s """, (name, last_name, password))

        result = cursor.fetchall()

    if result:
        return result[0]
    else:
        False

def get_date(password):
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "date_of_birth" 
        from public."managers" where "password" = %s """, (password,))

        result = cursor.fetchall()

    if result:
        return result[0]
    else:
        False

def get_practice(id):
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "Exercise" FROM public."practice" 
        WHERE "ID_practice" = %s""", (id))
        res = cursor.fetchall()
    return res

def get_prac_name(id):
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "Name" FROM public."practice" 
        WHERE "ID_practice" = %s""", (id))
        res = cursor.fetchall()
    return res

def insert_prac(_name, _content, _theme):
    with conn.cursor() as cursor:
        # Проверяем, существует ли _theme в таблице themes
        cursor.execute("""SELECT "ID_theme" FROM public."themes" WHERE "name" = %s""", (_theme,))
        theme_row = cursor.fetchone()

        if theme_row:
            # Если _theme уже существует, используем его ID_theme
            theme_id = theme_row[0]
        else:
            # Если _theme отсутствует, создаем новую запись в таблице themes
            cursor.execute(
                """INSERT INTO public."themes" ("name", "ID_theme") VALUES (%s, (SELECT COALESCE(MAX("ID_theme"), 0) + 1 FROM public."themes")) RETURNING "ID_theme" """,
                (_theme,))
            theme_id = cursor.fetchone()[0]

        cursor.execute("""SELECT MAX("ID_practice") FROM public."practice" """)
        mx = cursor.fetchone()[0] or 0
        # Записываем данные в таблицу practice
        cursor.execute("""
            INSERT INTO public."practice" ("ID_practice", "Name", "Exercise", "ID_theme")
            VALUES (%s, %s, %s, %s)
        """, (mx+1, _name, _content, int(theme_id)))

        return True

def insert_tasks(_name, _one, _two, _three, _four, _theme):
    with conn.cursor() as cursor:
        # Проверяем, существует ли _theme в таблице themes
        cursor.execute("""SELECT "ID_theme" FROM public."themes" WHERE "name" = %s""", (_theme,))
        theme_row = cursor.fetchone()

        if theme_row:
            # Если _theme уже существует, используем его ID_theme
            theme_id = theme_row[0]
        else:
            # Если _theme отсутствует, создаем новую запись в таблице themes
            cursor.execute(
                """INSERT INTO public."themes" ("name", "ID_theme") VALUES (%s, (SELECT COALESCE(MAX("ID_theme"), 0) + 1 FROM public."themes")) RETURNING "ID_theme" """,
                (_theme,))
            theme_id = cursor.fetchone()[0]

        cursor.execute("""SELECT MAX("ID_test") from public."tests" """)
        mx_test = cursor.fetchone()[0] or 0

        cursor.execute("""SELECT MAX("id_task") from public."task" """)
        mx_task = cursor.fetchone()[0] or 0

        cursor.execute("""INSERT INTO public."tests" ("ID_test", "ID_themes", "Name") VALUES (%s, %s, %s) """,
                       (mx_test+1 , theme_id, _name))

        cursor.execute(f"""INSERT INTO public."task" ("id_task", "id_test", "Task") VALUES ('{mx_task+1}', '{mx_test}', '{_one}'),
        ('{mx_task+2}', '{mx_test}', '{_two}'), ('{mx_task+3}', '{mx_test}', '{_three}'), ('{mx_task+4}', '{mx_test}', '{_four}')""")

    return True

class groups_functions():

    def add_isp(self, num):
        with conn.cursor() as cursor:
            cursor.execute(f"""SELECT "ID_user", "Nick", "Email", "Rating", "Progress" 
                              From public."User" 
                              Join public."groups" ON "User"."group_id" = "groups"."group_id"
                              where "User"."group_id" = {num}""")

            res = cursor.fetchall()

        return res

    def _delete_student(self, num):
        with conn.cursor() as cursor:
            cursor.execute("""
                        DELETE FROM public."User"
                        WHERE "ID_user" = %s
                    """, (num,))

            cursor.execute("""
                        DELETE FROM public."Ratings"
                        WHERE "id_user" = %s
                    """, (num,))
import psycopg2
from faker import Faker


fake = Faker()


def seed_users(n, cur):
    for _ in range(n):
        fullname = fake.name()
        email = fake.unique.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

def seed_tasks(n, cur):
    cur.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cur.fetchall()]
    
    cur.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cur.fetchall()]
    
    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.text()
        status_id = fake.random_element(status_ids)
        user_id = fake.random_element(user_ids)
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", 
                    (title, description, status_id, user_id))

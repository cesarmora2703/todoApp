import firebase_admin
from firebase_admin import credentials, firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()

# Get all users


def get_users():
    return db.collection('users').get()

# Get user info


def get_user(user_id):
    return db.collection('users').document(user_id).get()

# Register a new user, writes user data in Firebase


def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})

# Get todos


def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()

# Add todos for a current user


# Writes todos data in Firebase database
def put_todo(user_id, description):
    todos_collection_ref = db.collection(
        'users').document(user_id).collection('todos')
    todos_collection_ref.add({'description': description, 'done': False})

# Delete a selected todo for a current user


def delete_todo(user_id, todo_id):
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.delete()

# Toggle state of done flag, boolean


def update_todo(user_id, todo_id, done):
    todo_done = not bool(done)
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({'done': todo_done})

# Private function that ibtains reference for a todo_do document


def _get_todo_ref(user_id, todo_id):
    return db.document('users/{}/todos/{}'.format(user_id, todo_id))

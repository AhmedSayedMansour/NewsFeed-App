from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='newsfeed_app'
    )
    return connection

@app.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    content = data.get('content')
    user_id = data.get('user_id')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Post (user_id, content) VALUES (%s, %s)", (user_id, content))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Post created successfully'}), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    content = data.get('content')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Post SET content = %s WHERE post_id = %s", (content, post_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Post updated successfully'})

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Post WHERE post_id = %s", (post_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Post deleted successfully'})

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Post WHERE post_id = %s", (post_id,))
    post = cursor.fetchone()
    cursor.close()
    conn.close()

    if post:
        post_data = {
            'post_id': post[0],
            'user_id': post[1],
            'content': post[2],
            'created_at': post[3]
        }
        return jsonify(post_data)
    else:
        return jsonify({'message': 'Post not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

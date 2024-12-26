
const mysql = require('mysql2/promise');

const dbConfig = {
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
};

exports.createUser = async (event) => {
    const { name, email, age } = JSON.parse(event.body);

    try {
        const connection = await mysql.createConnection(dbConfig);
        const [results] = await connection.execute(
            'INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
            [name, email, age]
        );
        await connection.end();

        return {
            statusCode: 201,
            body: JSON.stringify({ message: 'User created!', id: results.insertId }),
        };
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ message: 'Error creating user', error }),
        };
    }
};
        
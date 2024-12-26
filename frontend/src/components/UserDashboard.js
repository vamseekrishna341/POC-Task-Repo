
import React, { useState, useEffect } from 'react';

function UserDashboard() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        const fetchUsers = async () => {
            const response = await fetch('<LAMBDA_ENDPOINT>/users');
            const data = await response.json();
            setUsers(data);
        };
        fetchUsers();
    }, []);

    return (
        <div>
            <h2>User Dashboard</h2>
            <ul>
                {users.map((user) => (
                    <li key={user.id}>{user.name} - {user.email}</li>
                ))}
            </ul>
        </div>
    );
}

export default UserDashboard;
                
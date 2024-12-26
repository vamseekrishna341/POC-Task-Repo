
import React, { useState } from 'react';

function UserForm() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [age, setAge] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch('<LAMBDA_ENDPOINT>', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email, age }),
        });
        const data = await response.json();
        console.log(data);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
            <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <input type="number" placeholder="Age" value={age} onChange={(e) => setAge(e.target.value)} />
            <button type="submit">Submit</button>
        </form>
    );
}

export default UserForm;
                
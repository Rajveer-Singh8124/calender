import React, { useEffect, useState } from 'react';
import CalendarComponent from './CalendarComponent';

function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        fetch('/api/hello')
            .then(response => response.json())
            .then(data => setMessage(data.message))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div className="App">
            <h1>{message}</h1>
            <CalendarComponent />
        </div>
    );
}

export default App;

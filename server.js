const express = require('express');
const app = express();
const PORT = 3000;

// Serve static files from the public folder
app.use(express.static('public'));

// Route to fetch API data
app.get('/api/posts', (req, res) => {
    const apiData = {
        userId: 1,
        id: 1,
        title: "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        body: "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    };
    res.json(apiData);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Basic test route to check if your server works
app.get('/', (req, res) => {
    res.json({ message: "Finance Tracker API is running smoothly!" });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

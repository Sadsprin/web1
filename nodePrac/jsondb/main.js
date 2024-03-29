import { join, dirname } from 'path'
import { Low, JSONFile } from 'lowdb'
import { fileURLToPath } from 'url'
const __dirname = dirname(fileURLToPath(import.meta.url));

// Use JSON file for storage
const file = join(__dirname, 'db.json')
const adapter = new JSONFile(file)
const db = new Low(adapter)

// Read data from JSON file, this will set db.data content
await db.read()

// If file.json doesn't exist, db.data will be null
// Set default data
// db.data = db.data || { posts: [] } // Node < v15.x
db.data ||= { posts: [] }             // Node >= 15.x

// Create and query items using plain J
db.data.posts.push('hello world')
console.log(db.data)
// You can also use this syntax if you prefer
const { posts } = db.data
posts.push('hello world')

// Write db.data content to db.json
await db.write()
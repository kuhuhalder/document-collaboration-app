const { Schema, model } = require("mongoose")

const Document = new Schema({
  _id: String,
  data: Object,
})

module.exports = model("Document", Document)
// import mongoose from 'mongoose';

// const documentSchema = mongoose.Schema({
//     _id: {
//         type: String,
//     },
//     data: {
//         type: Object,
//     }
// });

// const document = mongoose.model('Document', documentSchema);

// export default document;
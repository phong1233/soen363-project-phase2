const { MongoClient } = require("mongodb");
const csv = require("csv-parser");
const fs = require("fs");

const uri = "mongodb://127.0.0.1:27017";
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

async function run() {
  try {
    await client.connect();
    const db = client.db("soen363");
    await db.collection("hello").insertOne({ foo: 10 });
  } finally {
    await client.close();
  }
}

function convertData(data) {
  for (const property in data) {
    // Numbers
    if (data[property].length > 0 && !isNaN(data[property])) {
      data[property] = Number(data[property]);
      continue;
    }

    // Prices
    const priceRegex = /^\$\d+(\.\d*)?$/;
    if (data[property].match(priceRegex) !== null) {
      data[property] = Number(data[property].substring(1));
      continue;
    }

    // Percents
    const percentRegex = /^\d+\%?$/;
    if (data[property].match(percentRegex) !== null) {
      data[property] = Number(
        data[property].substring(0, data[property].length - 1)
      );
      continue;
    }

    // Dates
    const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (data[property].match(dateRegex) !== null) {
      data[property] = new Date(data[property]);
      continue;
    }

    // Booleans
    if (data[property] === "t") {
      data[property] = true;
      continue;
    }

    if (data[property] === "f") {
      data[property] = false;
      continue;
    }

    // Nulls
    if (data[property] === "N/A" || data[property] === "") {
      data[property] = null;
      continue;
    }
  }
}

async function loadListings() {
  const results = [];
  console.log("Loading listings...");

  fs.createReadStream("../dataset/listings.csv")
    .pipe(csv())
    .on("data", (data) => {
      convertData(data);
      results.push(data);
    })
    .on("end", async () => {
      try {
        const db = client.db("soen363");
        await db.collection("listings").insertMany(results);
      } finally {
        console.log("Listings added to the db.");
      }
    });
}

async function loadReviews() {
  const results = [];
  console.log("Loading reviews...");

  fs.createReadStream("../dataset/reviews.csv")
    .pipe(csv())
    .on("data", (data) => {
      convertData(data);
      results.push(data);
    })
    .on("end", async () => {
      try {
        const db = client.db("soen363");
        await db.collection("reviews").insertMany(results);
      } finally {
        console.log("Reviews added to the db.");
      }
    });
}

async function loadCalendar() {
  const results = [];
  console.log("Loading calendar...");

  fs.createReadStream("../dataset/calendar.csv")
    .pipe(csv())
    .on("data", (data) => {
      convertData(data);
      results.push(data);
    })
    .on("end", async () => {
      try {
        const db = client.db("soen363");
        await db.collection("calendar").insertMany(results);
      } finally {
        console.log("Calendar added to the db.");
      }
    });
}

async function load() {
  await client.connect();
  loadListings();
  loadReviews();
  loadCalendar();
}

load();

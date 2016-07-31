/*

datagen.js: generates random data for my_yelp database defined by the schema in my_yelp.sql.

npm install faker

To generate 1000000 restaurants:

node --max-old-space-size=2048 datagen.js restaurant 1000000 |psql my_yelp

To generate 1000000 reviewers:

node --max-old-space-size=2048 datagen.js reviewer 1000000 |psql my_yelp

To generate 1000000 reviews, where 200 is the current max ID for restaurants and 300 is the current max ID for reviewers:

node --max-old-space-size=2048 datagen.js review 1000000 1000000 1000000 |psql my_yelp

*/

var faker = require('faker');

function gen(tableName, times, genRow) {
  var keys;
  for (var i = 0; i < times; i++) {
    var row = genRow();
    if (i === 0) {
      keys = Object.keys(row);
      process.stdout.write('insert into ' + tableName + '(' + keys.join(', ') + ') values\n');
    }
    process.stdout.write('(')

    for (var j = 0; j < keys.length; j++) {
      var value = row[keys[j]];
      if (typeof value === 'string') {
        process.stdout.write("'" + value.replace(/'/g, "''") + "'");
      } else {
        process.stdout.write(String(value));
      }
      if (j < keys.length - 1) {
        process.stdout.write(',')
      }
    }

    process.stdout.write(')');

    if (i < times - 1) {
      process.stdout.write(',\n');
    }
  }
  process.stdout.write(';\n');
}

var table = process.argv[2];
var count = Number(process.argv[3]);

if (table === 'restaurant') {
  gen('restaurant', count, function() {
    return {
      name: faker.company.companyName()
    }
  });
} else if (table === 'reviewer') {
  gen('reviewer', count, function() {
    return {
      name: faker.name.findName(),
      karma: Math.ceil(Math.random() * 7)
    }
  });
} else if (table === 'review') {
  var numRestaurants = Number(process.argv[4]);
  var numReviewers = Number(process.argv[5]);
  gen('review', count, function() {
    return {
      title: faker.lorem.sentence(),
      content: faker.lorem.sentences(),
      stars: Math.ceil(Math.random() * 5),
      reviewer_id: Math.ceil(Math.random() * numReviewers),
      restaurant_id: Math.ceil(Math.random() * numRestaurants)
    }
  });
}

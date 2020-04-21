module.exports = async function (context, IoTHubMessage) {
  // dbName is name of database whilst collectionName i name of collection within dbName
  var dbName = "Messages";
  var collectionName = "IotGateway1";

  
  var mongoClient = require("mongodb").MongoClient;
  context.log('MongoClient created');

  // connection string to cosmosDB
  url = "cosmos connection string with mongo db api"
  const client = await mongoClient.connect(url,{useNewUrlParser: true, authSource: dbName})
        .catch(err => {context.log(err);});
  if (!client){
    context.log("failed to connect");
    context.done();
  }
  try {
    var collection = client.db(dbName).collection(collectionName);
    context.log(IoTHubMessage);
    let res = await collection.insertOne(IoTHubMessage);
    context.log(res);
    context.log("sent");
  } catch (err) {
      context.log("error");
    context.log(err);
  } 
  client.close();
  

  context.log("done");
  context.done();
};

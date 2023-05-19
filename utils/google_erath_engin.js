// // Load an image collection, filter it, and select the first image
// ee.Authenticate();
// ee.Initialize();


// var s2 = ee.ImageCollection('COPERNICUS/S2')
//           .filterDate('2021-01-01', '2021-12-31')
//           .filterBounds(geometry_1);
// var image = s2.first();

// // Add a polygon to the map
// Map.addLayer(geometry_1);

// // Create the export task
// var exportTask = ee.batch.Export.image.toDrive({
//   image: image.clip(geometry_1),
//   description: 'polygon_image',
//   folder: 'GEE_exports',
//   fileNamePrefix: 'polygon_image',
//   scale: 10,
//   region: geometry_1
// });

// // Start the export task



// exportTask.start();


// var s2 = ee.ImageCollection('COPERNICUS/S2')
//           .filterDate('2021-01-01', '2021-12-31')
//           .filterBounds(geometry_1);
// var image = s2.first();

// Assuming you have an EE Geometry object representing the selected polygon
// const selectedPolygon = ee.Geometry.Polygon([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]);

// Export the polygon as a feature to your Google Drive
Export.table.toDrive({
    collection: ee.FeatureCollection(geometry_1),
    description: 'selected_polygon',
    fileFormat: 'GeoJSON',
    folder : "Proactiveware"
  });
  











// Replace with your polygon coordinates
var polygon = ee.Geometry.Polygon(geometry_limon);

// // Convert the polygon to a feature
// var feature = ee.Feature(polygon, {});

// // Convert the feature to a GeoJSON string
// var geoJsonString = feature.toGeoJSONString();


// var polygon = ee.Geometry.Polygon([
//   [-122.090, 37.424],
//   [-122.084, 37.424],
//   [-122.084, 37.431],
//   [-122.090, 37.431]
// ]);

// Convert your polygon to a Feature object
var feature = ee.Feature(polygon, {});

// Export the FeatureCollection containing your polygon to your Drive as a GeoJSON file
// Export.table.toDrive({
//   collection: ee.FeatureCollection([feature]),
//   description: 'geometry_limon',
//   fileFormat: 'GeoJSON'
// });
Export.table.toDrive({
  collection: ee.FeatureCollection(geometry_limon),
  description: 'geometry_limon',
  fileFormat: 'GeoJSON',
  folder : "geojason"
});

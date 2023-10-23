/**
 * 
 * return an object viz:
 * {
 *      issue_type,
 *      count,
 * }
 */
var testData = [
    {
      "issue_type": "Warning",
      "created_date": "2019-05-13T13:43:16.437Z",
    },
    {
      "issue_type": "Warning",
      "created_date": "2019-05-13T13:45:16.330Z",
    },
    {
      "issue_type": "Alert",
      "created_date": "2019-05-13T13:43:16.437Z",
    },
    {
      "issue_type": "Alert",
      "created_date": "2019-05-13T13:45:16.330Z",
    }
  ]
  
  counts = testData.reduce((c, { issue_type: key }) => (c[key] = (c[key] || 0) + 1, c), {});
  
  console.log(counts);
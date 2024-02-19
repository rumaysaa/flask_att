const charts = document.querySelectorAll(".chart");

charts.forEach(async function (chart) {
  var ctx = chart.getContext("2d");
  const url = '/admin/cal_working_hour'
  const response = await (await fetch(url)).json()
  console.log(response)
  let i;
  var names = new Array();
  var hrs = new Array();
  for(i=0;i<response.length;i++){
    names.push(response[i].name)
    hrs.push(response[i].working_hrs)
  }
  var myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: names,
      datasets: [
        {
          label: "Today's hours",
          data: hrs,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});



$(document).ready(function () {
  $(".data-table").each(function (_, table) {
    $(table).DataTable();
  });
});

const express = require('express');
const ImageCharts = require('image-charts');
const ejs = require('ejs');
const path = require('path');
const fs = require('fs');
const csv = require('csv-parser');
const moment = require('moment');

const app = express();
const port = 3000;

app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));
app.set('view engine', 'ejs');

var lineChartUrl, pieChartUrl, barChartUrl, radarChartUrl = "";
let dataFromCSV = {};
let recordsCount = {};
let level_of_job = {};
let postingMonth = {};
let totalMonths = {};
let location = {};
let skills = {};
let totallocations={ };
let total_level = {
    EntryLevel: 0,
    MidLevel: 0,
    SeniorLevel:0
};

let chartTitles = {
    p: "Location-Wise Job Distribution",
    pa: "Seniority Level-Wise Job Distribution",
    bhg: "Top 10 Skills in Demand",
    lc: "Month-Wise Job Postings"
};

function readCSVFiles() {
    const csvFiles = ['jobs_DataAnalyst.csv', 'jobs_SoftwareEngineer.csv', 'jobs_QualityAssurance.csv'];

    for (const csvFile of csvFiles) {
        let count = 0;
        const jobCategory = csvFile.replace('jobs_', '').replace('.csv', ''); // Extract job category from filename
        const data = [];
        let filename = path.join("../Web Scrapping/test", csvFile);
        fs.createReadStream(filename)
            .pipe(csv())
            .on('data', (row) => {
                count += 1;
                data.push(row);
            })
            .on('end', () => {
                dataFromCSV[jobCategory] = data;
                level_of_job[jobCategory] = count_level(data);
                postingMonth[jobCategory] = jobMonths_Location(data, "date", totalMonths);
                location[jobCategory] = jobMonths_Location(data, "location", totallocations);
                skills[jobCategory]=skillset(data)
                recordsCount[jobCategory] = count;
            });
    }
}

readCSVFiles();

function sortJSONByMonth(json) {
  const monthOrder = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
  ];

  const sortedJSON = {};

  monthOrder.forEach(month => {
    if (json.hasOwnProperty(month)) {
      sortedJSON[month] = json[month];
    }
  });

  return sortedJSON;
} 
function toTitleCase(str) {
  return str.toLowerCase().replace(/(?:^|\s)\w/g, function(match) {
    return match.toUpperCase();
  });
}
function sortJSONByValues(json,n) {
  const sortedEntries = Object.entries(json).sort(([, valueA], [, valueB]) => {
      return valueB - valueA;
  });
    
    const topEntries = sortedEntries.slice(0, n);
  return Object.fromEntries(topEntries);
}
function count_level(data) {
    const level = {
        EntryLevel: 0,
        MidLevel:0,
        SeniorLevel:0
    };
    for (const entry of data){
        if (entry.level.includes('Entry') || entry.level.includes('Associate')) {
            level.EntryLevel += 1;
            total_level.EntryLevel += 1;
        }
        else if (entry.level.includes('Mid')) {
            level.MidLevel += 1;
            total_level.MidLevel += 1;
        }
        else {
            level.SeniorLevel += 1;
            total_level.SeniorLevel += 1;
        }
    }
    return level;
}

function skillset(data) {
    const result = {};
    for (const entry of data) {
        const skill = entry.skills;
        const elements = skill.split(','); 
        elements.forEach((element) => {
            const key = toTitleCase(element.trim()); // Remove leading and trailing spaces
            if (result[key]) {
            result[key]++;
            } else {
            result[key] = 1;
            }
        });
    }
     return result;
}
function jobMonths_Location(data, perimeter, All_Record) {
    const Record = {};
    for (const entry of data) {
        let key = "";
        if (perimeter != "location") {
             key = moment(entry.posted_date, 'YY-MMM').format('MMM');
        }
        else {
            key = entry.city;
        }
       if (Record[key] && All_Record[key]) {
           Record[key]++;
           All_Record[key]++;
      } else if (!Record[key] && !All_Record[key]){
           Record[key] = 1;
           All_Record[key] = 1;
        }
        else if (!Record[key] && All_Record[key]){
           Record[key] = 1;
           All_Record[key] ++;
        }

    }
    return Record;
}

function separateLabelsAndData(dataObject) {
  return Object.entries(dataObject).reduce(
    (result, [label, value]) => {
      result[0].push(label); // Push the label to the first array (labels)
      result[1].push(value); // Push the data to the second array (data)
      return result;
    },
    [[], []]
  );
}

app.get('/', (req, res) => {
    const selectedFilter = req.query.filter || "All";
    var data = [];
    var labels = [];
    if (selectedFilter == "SQA") {
        [radar_labels, radar_data] = separateLabelsAndData(level_of_job.QualityAssurance);
        [lc_labels, lc_data] = separateLabelsAndData(sortJSONByMonth(postingMonth.QualityAssurance));
        [pie_labels, pie_data] = separateLabelsAndData(location.QualityAssurance);
        [bar_labels, bar_data] = separateLabelsAndData(sortJSONByValues(skills.QualityAssurance,10));
    }
    else if (selectedFilter == "SoftwareEngineer") {
        [radar_labels, radar_data] = separateLabelsAndData(level_of_job.SoftwareEngineer);
        [lc_labels, lc_data] = separateLabelsAndData(sortJSONByMonth(postingMonth.SoftwareEngineer));
        [bar_labels, bar_data] = separateLabelsAndData(sortJSONByValues(skills.SoftwareEngineer,10));
        [pie_labels, pie_data] = separateLabelsAndData(location.DataAnalyst);
    }
    else if (selectedFilter == "DataAnalyst") {
        [radar_labels, radar_data] = separateLabelsAndData(level_of_job.DataAnalyst);
        [lc_labels, lc_data] = separateLabelsAndData(sortJSONByMonth(postingMonth.DataAnalyst));
        [pie_labels, pie_data] = separateLabelsAndData(location.DataAnalyst);
        [bar_labels, bar_data] = separateLabelsAndData(sortJSONByValues(skills.DataAnalyst,10));
    }
    else {
        [bar_labels, bar_data] = separateLabelsAndData(sortJSONByValues(recordsCount, 3));
        [radar_labels, radar_data] = separateLabelsAndData(total_level);
        [lc_labels, lc_data] = separateLabelsAndData(sortJSONByMonth(totalMonths));
        [pie_labels, pie_data] = separateLabelsAndData(totallocations);
    }
   lineChartUrl = generateChartUrl('lc', lc_data, lc_labels,selectedFilter); // Line chart
    barChartUrl = generateChartUrl('bhg', bar_data, bar_labels.reverse(),selectedFilter); // Bar chart
    radarChartUrl = generateChartUrl('pa', radar_data, radar_labels,selectedFilter); // radar chart
    pieChartUrl = generateChartUrl('p', pie_data,pie_labels,selectedFilter); // Pie chart

    // Render the HTML template with the chart URLs
    res.render('template', {
        lineChartUrl, barChartUrl,
        radarChartUrl, pieChartUrl, selectedFilter
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

function generateChartUrl(chartType, data, labels,selectedFilter) {
    let lineChartLabel = chartType === "lc" || chartType === "bhg" ? "" : labels.join("|");
    let axes = chartType === "bhg" ? "y,x" : "x,y";
    let chartTitle = "";
    if (selectedFilter != "All") {
        chartTitle = selectedFilter != "SQA" ? selectedFilter.replace(/([A-Z])/g, ' $1') + " " + chartTitles[chartType] : 
        selectedFilter+" "+chartTitles[chartType] ;
    }
    else if (chartType == "bhg" && selectedFilter == "All") {
        chartTitle = "Category-Wise Job Posting";
    }
    else {
        chartTitle = chartTitles[chartType];
    }
    const chart = ImageCharts()
        .cht(chartType)
        .chls("3")
        .chs('450x350')
        .chd(`t:${data.join(',')}`)
        .chxt(axes)
        .chxl(`0:|${labels.join('|')}`)
        .chco("FF00007F,00FF007F,0000FF7F")
        .chdl(lineChartLabel)
        .chma("15,15,15,15")
        .chtt(chartTitle)
        .toURL();
    
    return chart;
}



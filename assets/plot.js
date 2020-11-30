// Plot a chart of number of umpires by in IPL by country.
fetch('assets/foreign_umpire_analysis.json')
  .then(response => response.json())
  .then(data => {
      let country = Object.keys(data);
      let count_umpire = Object.values(data);

      Highcharts.chart('container_1', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Foreign umpire analysis'
        },
        subtitle: {
            text: 'chart of the total runs scored by each teams over the history of IPL.'
        },
        xAxis: {
            categories: country
        },
        yAxis: {
            labels: {
                x: -15
            },
            title: {
                text: 'Number of Umpires'
            }
        },
        series: [{
            name: 'Country',
            data: count_umpire
        }],
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                // Make the labels less space demanding on mobile
                chartOptions: {
                    xAxis: {
                        labels: {
                            formatter: function () {
                                return this.value.charAt(0);
                            }
                        }
                    },
                    yAxis: {
                        labels: {
                            align: 'left',
                            x: 0,
                            y: -2
                        },
                        title: {
                            text: ''
                        }
                    }
                }
            }]
        }
    });
    
    document.getElementById('small').addEventListener('click', () => {
        chart.setSize(400, 300);
    });
    
    document.getElementById('large').addEventListener('click', () => {
        chart.setSize(800, 300);
    });    
});


// plot the total runs scored by every batsman playing for Royal Challengers Bangalore over the history of IPL.
fetch('assets/top_batsman_for_royal_challengers_bangalore.json')
  .then(response => response.json())
  .then(data => {
      let batsman = Object.keys(data);
      let runs = Object.values(data);
      
      Highcharts.chart('container_2', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Top batsman for Royal Challengers Bangalore'
        },
        subtitle: {
            text: 'plot the total runs scored by every batsman playing for Royal Challengers Bangalore over the history of IPL.'
        },
        xAxis: {
            categories: batsman
        },
        yAxis: {
            labels: {
                x: -15
            },
            title: {
                text: 'Total Runs Scored'
            }
        },
        series: [{
            name: 'Batsman Playing for Royal Challengers Bangalore',
            data: runs
        }],
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                // Make the labels less space demanding on mobile
                chartOptions: {
                    xAxis: {
                        labels: {
                            formatter: function () {
                                return this.value.charAt(0);
                            }
                        }
                    },
                    yAxis: {
                        labels: {
                            align: 'left',
                            x: 0,
                            y: -2
                        },
                        title: {
                            text: ''
                        }
                    }
                }
            }]
        }
    });
    
    document.getElementById('small').addEventListener('click', () => {
        chart.setSize(400, 300);
    });
    
    document.getElementById('large').addEventListener('click', () => {
        chart.setSize(800, 300);
    });
});


// Plot a chart of the total runs scored by each teams over the history of IPL. 
fetch('assets/total_runs_scored_by_team.json')
  .then(response => response.json())
  .then(data => {
      let teams = Object.keys(data);
      let runs = Object.values(data);

      Highcharts.chart('container_3', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Total runs scored by team'
        },
        subtitle: {
            text: 'chart of the total runs scored by each teams over the history of IPL.'
        },
        xAxis: {
            categories: teams
        },
        yAxis: {
            labels: {
                x: -15
            },
            title: {
                text: 'total runs scored '
            }
        },
        series: [{
            name: 'Teams',
            data: runs
        }],
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                // Make the labels less space demanding on mobile
                chartOptions: {
                    xAxis: {
                        labels: {
                            formatter: function () {
                                return this.value.charAt(0);
                            }
                        }
                    },
                    yAxis: {
                        labels: {
                            align: 'left',
                            x: 0,
                            y: -2
                        },
                        title: {
                            text: ''
                        }
                    }
                }
            }]
        }
    });
    
    document.getElementById('small').addEventListener('click', () => {
        chart.setSize(400, 300);
    });
    
    document.getElementById('large').addEventListener('click', () => {
        chart.setSize(800, 300);
    });
});

// Stacked chart of matches played by team by season
fetch('assets/stacked_chart_of_matches_played_by_team_by_season.json')
  .then(response => response.json())
  .then(data => {
      let years = data.years
      let team_score = data.team_data

      Highcharts.chart('container_4', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Stacked chart of matches played by team by season'
        },
        xAxis: {
            categories: years
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Matches Played by Team'
            }
        },
        legend: {
            reversed: true
        },
        plotOptions: {
            series: {
                stacking: 'normal'
            }
        },
        series: team_score
    });
});

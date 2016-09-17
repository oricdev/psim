/**
 * Created by olivier on 14.09.16.
 */

/* Data Set */
var dataSet = [];
/* Control-ids of the page where to log messages and extra content */
var log_ctrlid="#logDetails";
var log_class_normal="logNormal";
var log_class_warning="logWarning";
var log_class_important="logImportant";
var log_class_failure="logError";
/* Number of requests sent, and those in failure */
var nbRequestsData=0;
var nbRequestsError=0;


function requestNextData() {
    if (nbRequestsData==0) {
        $("<p class=''" + log_class_normal + "'>").text("["+nbRequestsData+"] Initializing data-set..").appendTo(log_ctrlid);
    } else {
        $("<p class=''" + log_class_normal + "'>").text("["+nbRequestsData+"] fetching data..").appendTo(log_ctrlid);
    }
    nbRequestsData++;
    /* Ajax request */
    /*$.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + "/todo/",
        contentType: "application/json; charset=utf-8",
        data: {id: 745},
        success: function (data) {
            $("<p class='logText'>").text(data.value).appendTo("#logDetails");
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            $("<p class=''" + log_class_failure + "'>").text("["+nbRequestsError+"] "+textStatus+" :: "+errorThrown).appendTo(log_ctrlid);
        }
    });*/

    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + "/getslotsdata/",
        contentType: "application/json; charset=utf-8",
        data: {timegap: 1000, nbslots: 10},
        success: function (data) {
            $("<p class='logText'>").text(data.value).appendTo("#logDetails");
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            $("<p class=''" + log_class_failure + "'>").text("["+nbRequestsError+"] "+textStatus+" :: "+errorThrown).appendTo(log_ctrlid);
        }
    });
}

function checkRequestOfDataNeeded(nbDataToFetch, ptrCurrent, ptrLastFetch, percentageConsumptionMax) {
    var isNeeded = false;
    $("<p class='logText'>").text("checking again..").appendTo("#logDetails");
    /* Check if the percentage of consumption of data since last fetch exceeded the percentage [percentConsumptionBeforeNewFetch] */
    isNeeded = (dataSet.length == 0 || ((ptrCurrent - ptrLastFetch) / nbDataToFetch) >= percentageConsumptionMax);
    return isNeeded;
}
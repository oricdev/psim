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


function initSystem() {
    $("<p class='" + log_class_normal + "'>").text("[.] Initializing the system..").appendTo(log_ctrlid);
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + "/initsystem/",
        contentType: "application/json; charset=utf-8",
        success: function (data) {
            /* data fetched from system:
            - current_rel_time (int)
            - timegap (ms)
            - nb_actors + their names_actors
            - nb_receivers + their names_receivers
            - nb_actors_receivers + their names_actors_receivers
             */
            $("<p class='logText'>").text("[.] system initialized and ready to start:").appendTo("#logDetails");
            $("<p class='logSubText'>").text("[.] relative time: "+data['system_rel_time']).appendTo("#logDetails");
            $("<p class='logSubText'>").text("[.] time-slot: "+data['timegap']+" ms").appendTo("#logDetails");
            $("<p class='logSubText'>").text("[.] nb of actors: "+data['actors'].length+" ("+data['actors'].toString()+")").appendTo("#logDetails");
            $("<p class='logSubText'>").text("[.] nb of receivers: "+data['receivers'].length+" ("+data['receivers'].toString()+")").appendTo("#logDetails");
            $("<p class='logSubText'>").text("[.] nb of actors/receivers: "+data['actors_receivers'].length+" ("+data['actors_receivers'].toString()+")").appendTo("#logDetails");
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            nbRequestsError++;
            $("<p class=''" + log_class_failure + "'>").text("[./"+nbRequestsError+"] "+textStatus+" :: "+errorThrown).appendTo(log_ctrlid);
        }
    });
}

function requestNextData() {
    var cur_nbRequestsData = nbRequestsData;
    if (cur_nbRequestsData==0) {
        $("<p class=''" + log_class_normal + "'>").text("["+cur_nbRequestsData+"] Initializing data-set..").appendTo(log_ctrlid);
    } else {
        $("<p class=''" + log_class_normal + "'>").text("["+cur_nbRequestsData+"] fetching data..").appendTo(log_ctrlid);
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
        data: {ptrlast: 0, nbslots: 10},
        success: function (data) {
            $("<p class='logText'>").text("["+cur_nbRequestsData+"] "+data.value).appendTo("#logDetails");
            /* todo: append data and update ptrLastFetch */
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            nbRequestsError++;
            $("<p class=''" + log_class_failure + "'>").text("["+cur_nbRequestsData+"/"+nbRequestsError+"] "+textStatus+" :: "+errorThrown).appendTo(log_ctrlid);
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
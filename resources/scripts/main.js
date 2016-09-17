/**
 * Created by olivier on 14.09.16.
 */


function doLoop() {
    /* Retrieve next data-set if required */
    if (checkRequestOfDataNeeded(nbDataToFetch, ptrCurrent, ptrLastFetch, percentageConsumptionBeforeNewFetch)) {
        requestNextData();
    }
    consumeData();
    return true
}

function consumeData() {

}
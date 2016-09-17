/**
 * Created by olivier on 14.09.16.
 */
/* Setting parameters for THIS application */

/* Data Set is defined in servicing.js since the callback function itself feeds the dataSet with extra data:
* no use of dataSet as parameter and close encapsulation instead */

/* Number of data-items for a fetch */
var nbDataToFetch = 5;
/* Percentage before requesting more data to feed the dataSet (asynchroneous/ajax) */
var percentageConsumptionBeforeNewFetch = 0.70;
/* Current pointer */
var ptrCurrent = 0;
/* Pointer since last data fetch */
var ptrLastFetch=0;
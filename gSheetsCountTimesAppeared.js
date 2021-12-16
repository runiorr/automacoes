var UB = 0;
var UI = 0;
var UA = 0;

function setUsersCount() {
 var fromColumn = 'G'    // Escolhe a coluna a ser iterada - EX: 'G'
 var startRow = 4         // Escolhe a linha inicial - EX: 4
 var howManyRows = 244     // Escolhe quantas linhas - EX: 2
 var column = getFullColumn (fromColumn, startRow);
 var data = column.getValues();
 iterateRow(data, howManyRows);
 storeValue("J3", UB) // Escolher qual célula vai sobrescrever - EX: "J3"
 storeValue("K3", UI) // Escolher qual célula vai sobrescrever - EX: "K3"
 storeValue("L3", UA) // Escolher qual célula vai sobrescrever - EX: "L3"
}

function iterateRow (data, howManyRows) {
 for (var i = 0; i <= howManyRows; i++) {
   let rowArray = data[i];
   let splitString = rowArray[0].split("+");
   for (var j = 0; j < splitString.length; j++) {
     if (splitString[j] == " 1UB ") { // Escolher variável a ser procurada - EX: " 1UB "
       UB = UB + 1;
     } else if (splitString[j] == " 1UI ") { // Escolher variável a ser procurada - EX: " 1UI "
       UI = UI + 1;
     } else if (splitString[j] == " 1UA ") { // Escolher variável a ser procurada - EX: " 1UA "
       UA = UA + 1;
     }
   }
 }
}

function storeValue(cellPosition, newValue) {
 var Sheets = SpreadsheetApp.openByUrl("SPREADSHEET_URL").getSheetByName("SHEET_NAME");
 var cell = Sheets.getRange(cellPosition);
 cell.setValue(newValue);
}

function getFullColumn(column, startRow){
 var Sheets = SpreadsheetApp.openByUrl("SPREADSHEET_URL").getSheetByName("SHEET_NAME");
 var lastRow = Sheets.getLastRow();
 return Sheets.getRange(column+startRow+':'+column+lastRow);
}

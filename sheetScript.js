//@OnlyCurrentDoc
var X = 0;
var Y = 0;
var Z = 0;

function setUsersCount() {
  var fromColumn = 'G'    // Escolhe a coluna a ser iterada - EX: 'G'
  var fromRow = 4         // Escolhe a linha inicial - EX: 4
  var toRow = 10          // Escolhe a linha final - EX: 10
  var column = getFullColumn (fromColumn, fromRow);
  var data = column.getValues();
  iterateRow(data, toRow);
  storeValue(0, "H1", X) // Escolher qual célula vai sobrescrever - EX: "H1"
  storeValue(0, "H2", Y) // Escolher qual célula vai sobrescrever - EX: "H2"
  storeValue(0, "H3", Z) // Escolher qual célula vai sobrescrever - EX: "H3"
}

function iterateRow (data, toRow) {
  for (var i = 0; i < toRow; i++) {
    var splitString = data[i][0].split("+");
    for (var j = 0; j < splitString.length; j++) {
      if (splitString[j] == " 1UB ") {                    // Escolher variável a ser procurada - EX: " 1UB "
        UB = UB + 1;
      } else if (splitString[j] == " 1UI ") {             // Escolher variável a ser procurada - EX: " 1UI " 
        UI = UI + 1;
      } else if (splitString[j] == " 1UA ") {             // Escolher variável a ser procurada - EX: " 1UA "
        UA = UA + 1;
      }
    }
  }
}

function storeValue(sheetPosition, cellPosition, newValue) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[sheetPosition];
  var cell = sheet.getRange(cellPosition); 
  cell.setValue(newValue);
}

function getFullColumn(column, startIndex) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  var lastRow = sheet.getLastRow();
  return sheet.getRange(column+startIndex+':'+column+lastRow);
}

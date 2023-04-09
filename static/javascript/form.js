const button1 = document.getElementById('button1');
const button2 = document.getElementById('button2');
const table1 = document.getElementById('first');
const table2 = document.getElementById('second');

button1.addEventListener('click', () => {
  table1.style.display = 'inline-table'; // Update this line
  table2.style.display = 'none';
  button1.style.backgroundColor = "rgb(71, 114, 192)";
 button2.style.backgroundColor = "rgb(181, 199, 229)";
 button1.style.color = "white";
 button2.style.color = "black";
  
});

button2.addEventListener('click', () => {
  table1.style.display = 'none';
  table2.style.display = 'inline-table'; // Update this line

  button2.style.backgroundColor = "rgb(71, 114, 192)";
button1.style.backgroundColor = "rgb(181, 199, 229)";
button2.style.color = "white";
 button1.style.color = "black";
});


// display: inline-table;
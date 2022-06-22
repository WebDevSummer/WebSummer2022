const container = document.querySelector('.container');
var inputValue = document.querySelector('.input');
const add = document.querySelector('.add');


var todosEX = window.localStorage.getItem("todos");
var todos = JSON.parse(todosEX);


class item{
    
	constructor(name){
		this.createItem(name);
	}

    createItem(name){
    	var itemBox = document.createElement('div');
        itemBox.classList.add('item');

    	var input = document.createElement('input');
    	input.type = "text";
    	input.disabled = true;
    	input.value = name;

    	input.classList.add('item_input');
        

    	var remove = document.createElement('button');
    	remove.classList.add('remove');
    	remove.innerHTML = "<img src=\"images.png\" width=\"18px\">";
    	remove.addEventListener('click', () => this.remove(itemBox, name));

        var checkbox = document.createElement('input');
        checkbox.setAttribute('type', 'checkbox');
        checkbox.className = "taskCheck";
      

    	container.appendChild(itemBox);

        itemBox.appendChild(checkbox);
        itemBox.appendChild(input);
        itemBox.appendChild(remove);


    }

    remove(itemBox, name){
        itemBox.parentNode.removeChild(itemBox);
        let index = todos.indexOf(name);
        todos.splice(index, 1);
        window.localStorage.setItem("todos", JSON.stringify(todos));
    }


};

add.addEventListener('click', check);

function check(){
	if(inputValue.value != ""){
		new item(inputValue.value);
        todos.push(inputValue.value);
        window.localStorage.setItem("todos", JSON.stringify(todos));
		inputValue.value = "";
	}
}

for (var v = 0 ; v < todos.length; v++){
    new item(todos[v]);
}
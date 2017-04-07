var ViewModel = function() {
    this.credits = ko.observable();
    this.username = ko.observable();
    this.ships = ko.observable();
};

function init() {
	getPlayer();
	getShips();
}

var viewModel = new ViewModel();

ko.applyBindings(viewModel);


function getPlayer() {
	$.ajax({
		url: 'get_player',
		type: 'GET',
		async: false,
		timeout: 30000,
		error: function(data) {
			console.log('Error: ' + data);
		},
		success: function(data) {
			viewModel.credits(data['fields']['credits']);
			viewModel.username(data['fields']['name']);
		}
	});
}

function getShips() {
	$.ajax({
		url: 'get_ships',
		type: 'GET',
		async: false,
		timeout: 30000,
		error: function(data) {
			console.log('Error: ' + data);
		},
		success: function(data) {
			viewModel.ships(data['fields']);
			console.log(data);
		}
	});
}

init();

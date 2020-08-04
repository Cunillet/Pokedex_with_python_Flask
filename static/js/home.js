
let ns = {};

// Model instance
ns.model = (function () {
	'use strict';

	let $event_pump = $('body');

	// return the API
	return {
		'read': function() {
			let ajax_options = {
				type: 'GET',
				url: 'api/pokemon',
				accepts: 'application/json',
				dataType: 'json'
			};
			$.ajax(ajax_options)
			.done(function(data) {
				$event_pump.trigger('model_read_success', [data]);
			})
			.fail(function(xhr, textStatus, errorTrhown) {
				$event_pump.trigger('model_error', [xhr, textStatus, errorTrhown]);
			})
		}
	};
}());

// create the view instance
ns.view = (function() {
	'use strict';

	let $popemon_id = $('#pokemon_id'),
		$name = $('#name'),
		$ptype = $('#ptype'),
		$weight = $('#weight'),
		$height = $('#height');

	// return the API
	return {
		build_table: function(pokemons) {

			// clear the table
			$('.pokemons table > tbody').empty();

			// check for a list of pokemons
			if (pokemons) {
				let rows = ''
				for (let i=0, l=pokemons.length; i < pokemons.length; i++) {
					rows += `<tr data-pokemon-id="${pokemons[i].pokemon_id}">
						<td class="pokemon_id">${pokemons[i].pokemon_id}</td>
						<td class="name">${pokemons[i].name}</td>
						<td class="ptype">${pokemons[i].ptype}</td>
						<td class="weight">${pokemons[i].weight}</td>
						<td class="height">${pokemons[i].height}</td>
					</tr>`;
				}
				$('.pokemons table > tbody').append(rows);
			}
		},
		error: function(error_msg) {
			$('.error')
				.text(error_msg)
				.css('visibility', 'visible');
			setTimeout(function() {
				$('.error').css('visibility', 'hidden');
			}, 3000);
		}
	};
}());

// create the controller
ns.controller = (function (m, v) {
	'use strict';

	let model = m,
		view = v,
		$event_pump = $('body'),
		$pokemon_id = $('#pokemon_id');

	// get data from model after controller is done initializing
	setTimeout(function() {
		model.read();
	}, 1000);

	// handle model events
	$event_pump.on('model_read_success', function(e, data) {
		view.build_table(data);
		view.reset();
	});

	$event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
		let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
		view.error(error_msg);
		console.log(error_msg);
	})
}(ns.model, ns.view));


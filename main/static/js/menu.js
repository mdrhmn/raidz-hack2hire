$(document).ready(function () {
	var $category = $('.card-category'),
		$filters = $("#filters input[type='checkbox']"),
		product_filter = new ProductFilterLevel1($category, $filters);
	product_filter.init();
});

function ProductFilterLevel1(category, filters) {
	var _this = this;

	this.init = function () {
		this.category = category;
		this.filters = filters;
		this.bindEvents();
	};

	this.bindEvents = function () {
		this.filters.click(this.filterGridProducts);
		$('#none').click(this.removeAllFilters);
	};

	this.filterGridProducts = function () {
		_this.category.hide();
		var selectedFilters = _this.filters.filter(':checked');
		if (selectedFilters.length) {
			var selectedFiltersValues = [];
			selectedFilters.each(function () {
				var currentFilter = $(this);
				selectedFiltersValues.push("[data-" + currentFilter.attr('name') + "='" + currentFilter.val() + "']");
			});
			_this.category.filter(selectedFiltersValues.join(',')).show('1000');
		} else {
			_this.category.show('1000');
		}
	};

	this.removeAllFilters = function () {
		_this.filters.prop('checked', false);
		_this.category.show('1000');
	}
}

$(document).on("click", "#event-reg-modal-pop", function () {
    $.ajax({
        url: $(this).attr("data-url"),
        success: function (data) {
            $("#event-reg-modal-container").html(data);
            $('#event-reg-modal').modal('toggle');
        }
    });
});
$(document).ready(function(){
	$(".ajaxLoader").hide();


	// Product Filter Start
	$(".filter-checkbox,#priceFilterBtn").on('click',function(){
		var _filterObj={};
		var _minPrice=$('#maxPrice').attr('min');
		var _maxPrice=$('#maxPrice').val();
		_filterObj.minPrice=_minPrice;
		_filterObj.maxPrice=_maxPrice;


		$(".filter-checkbox").each(function(index,ele){
			var _filterVal=$(this).val();
			var _filterKey=$(this).data('filter');
			// console.log(_filterKey, _filterVal)
			_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
				return el.value;
			});
		});


		document.getElementById("brands").addEventListener("click", function() {
			$(".filter-checkbox").each(function(index,ele){					
				var _filterVal=$(this).val();
				var _filterKey=$(this).data('filter');
		
				_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
					return el.value;
				});
			});
			console.log("Brand=",_filterObj)
			// Run Ajax
			$.ajax({
				url:'/filter',
				data:_filterObj,
				dataType:'json',
				beforeSend:function(){
					$(".ajaxLoader").show();
				},
				success:function(res){
					// console.log(res);
					$("#filteredProducts").html('');
					$("#filteredProducts").html(res.product_ajax);
					// console.log(res.product_ajax)

					// $("#brands").html('');
					// $("#brands").html(res.brand_ajax);
					// console.log("Brand=",res.brand)

					$(".ajaxLoader").hide();
				}
			});	
		});
	
		console.log("Final=",_filterObj)

		// Run Ajax
		$.ajax({
			url:'/filter',
			data:_filterObj,
			dataType:'json',
			beforeSend:function(){
				$(".ajaxLoader").show();
			},
			success:function(res){
				// console.log(res);
				$("#filteredProducts").html('');
				$("#filteredProducts").html(res.product_ajax);
				// console.log(res.product_ajax)

				$("#brands").html('');
				$("#brands").html(res.brand_ajax);
				// console.log("Brand=",res.brand)

				$(".ajaxLoader").hide();
			}
		});


		// // Run Axios Ajax
		// axios.get(`/filter`,{params:_filterObj})
		// .then(res=>{
		// 	$("#filteredProducts").html('');
		// 	$("#filteredProducts").html(res.data.product_ajax);

		// 	$(".brands").html('');
		// 	$(".brands").html(res.data.brand_ajax);

		// 	// console.log("Brand=",res.data.brand)
		// }).catch(err=> { console.log(err)})


	});
	// End

	


	

	// Filter Product According to the price
	$("#maxPrice").on('blur',function(){
		var _min=$(this).attr('min');
		var _max=$(this).attr('max');
		var _value=$(this).val();
		console.log(_value,_min,_max);
		if(_value < parseInt(_min) || _value > parseInt(_max)){
			alert('Values should be '+_min+'-'+_max);
			$(this).val(_min);
			$(this).focus();
			$("#rangeInput").val(_min);
			return false;
		}
	});
	// End
});
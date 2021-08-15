try {
    var $eventSelect2 = $("#selectjs-1-1")
    $eventSelect2.select2({
        placeholder: "Type",
        ajax: {
            type: "GET",

            dataType: 'json',
            url: function (params) {
                loca = 'loadMore/' + params.term
                console.log(loca)
                return loca
            },

            processResults: function (data) {

                lista = []
                for (d in data) {
                    lista.push(data[d])
                }

                var fin = []
                fin = data

                return {


                    results: $.map(fin, function (item) {


                            $eventSelect2.on("select2:select", function (e) {
                                nom = e.params.data.id
                                valeur = e.params.data.text
                                var $newOption = $("<option selected='selected'></option>").val(valeur).text(nom)

                                $("#selectjs-1-1").append($newOption).trigger('change');
                            })

                            return {
                                text: item.id_article,
                                id: item.nom_article

                            }

                        }

                    )

                }



            },
            cache: true,


        }
    })
} catch (error) {
    console.log('not here')
}
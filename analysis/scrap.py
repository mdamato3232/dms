# Get dataset ready for radio pie chart.
        radio_dataset = queryset_list \
          .values('radio_type') \
          .exclude(radio_type='') \
          .annotate(total=Count('radio_type')) \
          .order_by('radio_type')
        # pdb.set_trace()
        chart = {
          'chart': {'type': 'pie'},
          'title': {'text': 'Transmissions by Radio Type'},
          'series': [{
            'name': 'Transmissions',
            'data': list(map(lambda row: {'name': row['radio_type'], \
              'y': row['total']}, radio_dataset))
          }]
        }
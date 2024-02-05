if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data_filtered = data[(data['passenger_count']!=0)&(data['trip_distance']!=0)]

    data_filtered['lpep_pickup_date']=data_filtered['lpep_pickup_datetime'].dt.date

    data_filtered.columns = (data_filtered.columns.str.replace(' ','_').str.lower())

    print(data_filtered['vendorid'].unique())

    return data_filtered


@test
def test_passenger_count(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum()==0

@test
def test_trip_distance(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum()==0

@test
def test_vendorid(output,*args)-> None:
    assert 'vendorid' in output.columns



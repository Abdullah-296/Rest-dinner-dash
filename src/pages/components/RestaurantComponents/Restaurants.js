import React, {useState, useEffect} from 'react'
import axios from "axios";

import '../../Style/Restaurant.css'
import { Restaurantblock } from './Restaurantblock';

export const Restaurants = () => {

  const [baseURL, setbaseURL] = useState("https://food-bear.herokuapp.com/api/getrestaurant/")

  const [Restaurantdata, setRestaurantdata] = useState({
    'count': 0,
    'next': '',
    'previous': '',
    'data': [],
  });

  const getrestaurantdata = () => {
    axios.get(baseURL)
    .then((response) => {
      setRestaurantdata({
         'count': response.data['count'],
         'next': response.data['next'],
         'previous': response.data['previous'],
         'data': response.data['results']
         });

      })
    };


    useEffect(() => {
      getrestaurantdata();
 }, [baseURL]);


 const changeurlp = () =>{
  setbaseURL(Restaurantdata['previous'])
}

const changeurln = () =>{
  setbaseURL(Restaurantdata['next'])
}

  return (
    <div>

      <div className="category-heading my-3 py-3">
       <h2>Restaurants</h2>
      </div>


      <div className='item-main-container'>
      {Restaurantdata.data.map((restaurant) =>
      < Restaurantblock key={restaurant.id} restaurant={restaurant}/>

      )}
      </div>


        <div className='pagination'>
          <button disabled={!Restaurantdata['previous']} className='btn btn-primary' onClick={changeurlp}> Previous page</button>
          <button disabled={!Restaurantdata['next']} className='btn btn-primary' onClick={changeurln}> Next page</button>
        </div>



    </div>
  )
}

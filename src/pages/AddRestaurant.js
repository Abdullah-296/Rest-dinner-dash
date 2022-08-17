import React, {useState} from 'react'
import { Navbar } from './components/Navbar';
import { Hero } from './components/Hero';

import './Style/Form.css';

export const AddRestaurant = () => {

  const [Restaurantinfo, setRestaurantinfo] = useState({
    title: "",
    Address: "",
    Owner: "",
    description: "",
    image: null
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(Restaurantinfo);
  };

  const checkvalidation = (event) => {
    console.log(event.target.value);
    console.log(event.target.name);
    if (event.target.name === 'title'){

    }

  }

  const handleChange = (event) => {
    setRestaurantinfo({ ...Restaurantinfo, [event.target.name]: event.target.value });
    checkvalidation(event);
  };

  const handlefile = (event) => {
    setRestaurantinfo({ ...Restaurantinfo, [Restaurantinfo.image]: event.target.files[0] });
  }

  return (
    <div>
      <Navbar />
      <Hero />

      <div className='form-container'>

        <div className='container'>
          <h1 className='heading'> Add Restaurant </h1>

          <form>
            <fieldset>

              <div className="form-group">
                <label htmlFor="Name">Restaurant Name:</label>
                <input type="text" className="form-control" id="Name"  placeholder="i-e KFC" name='title' value={Restaurantinfo.title} onChange={handleChange} required={true}/>
              </div>

              <div className="form-group">
                <label htmlFor="RestaurantAddress">Restaurant Address:</label>
                <textarea className="form-control" id="RestaurantAddress" rows="3" placeholder='I 10 Islamabad' name='Address' value={Restaurantinfo.Address} onChange={handleChange}  required ></textarea>
              </div>

              <div className="form-group">
                <label htmlFor="RestaurantAddress">Owner:</label>
                <select className="form-control" name='Owner' value={Restaurantinfo.Owner} onChange={handleChange}    >
                  <option>Default select</option>
                  <option>Admin</option>
                  <option>Abdullah</option>
                  <option>Test</option>
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="description">Description:</label>
                <textarea className="form-control" id="description" rows="3" placeholder='Provide good tasty food'  name='description' value={Restaurantinfo.description} onChange={handleChange} ></textarea>
              </div>

              <div className="form-group">
                <label htmlFor="formFile" className="form-label">Default file input example</label>
                <input className="form-control" type="file" id="formFile" name='image' onChange={handlefile}/>
              </div>

              <button type="submit" className="btn btn-primary" onClick={handleSubmit}>Add Restaurant</button>
            </fieldset>
          </form>

        </div>
      </div>

    </div>
  )
}

import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import {RestaurantDisplay} from './pages/RestaurantDisplay';
import {ItemDisplay} from './pages/ItemDisplay';
import {Cart} from './pages/Cart';
import {AdminDashboard} from './pages/AdminDashboard';
import {ItemDetail} from './pages/ItemDetail';
import {AddRestaurant} from './pages/AddRestaurant';
import {Login} from './pages/Login';
import {PageNotFound} from './pages/PageNotFound';
import { AuthProvider } from "./context/Authcontext";
import {Protectedroute} from "./context/Protectedroute";
import { Registeruser } from './pages/Registeruser';



function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <AuthProvider>

        <Routes>
            <Route exact path="/" element={<RestaurantDisplay />} />
            <Route exact path="/restaurant/:restaurantid" element={<ItemDisplay />} />
            <Route exact path="/item/:itemid" element={<ItemDetail />} />
            <Route exact path="/cart" element={<Cart />} />

            {/* <Route exact path="/admin" element={<AdminDashboard />} /> */}
            {/* <Protectedroute element={<AdminDashboard />} path="/admin" exact /> */}


            <Route exact path='/admin' element={<Protectedroute/>}>
              <Route exact path='/admin' element={<AdminDashboard/>}/>
            </Route>


            <Route exact path="/addrestaurant" element={<AddRestaurant />} />
            <Route exact path="/login" element={<Login />} />

            <Route exact path="/registeruser" element={<Registeruser />} />

            <Route path="/*" element={<PageNotFound />} />

        </Routes>


      </AuthProvider>

    </BrowserRouter>
    </div>
  );
}

export default App;

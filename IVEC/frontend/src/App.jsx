import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Dashboard from './pages/Dashboard';
import InvestmentDetail from './pages/InvestmentDetail';
import Transactions from './pages/Transactions';
import './styles/main.css';

const App = () => {
    return (
        <Router>
            <Header />
            <Switch>
                <Route path="/" exact component={Dashboard} />
                <Route path="/investment/:id" component={InvestmentDetail} />
                <Route path="/transactions" component={Transactions} />
            </Switch>
            <Footer />
        </Router>
    );
};

export default App;
import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
    return (
        <header className="header">
            <div className="logo">
                <h1>IVEC</h1>
            </div>
            <nav className="nav">
                <ul>
                    <li><Link to="/">Dashboard</Link></li>
                    <li><Link to="/investments">Investments</Link></li>
                    <li><Link to="/transactions">Transactions</Link></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
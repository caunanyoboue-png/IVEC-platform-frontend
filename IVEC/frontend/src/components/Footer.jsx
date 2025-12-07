import React from 'react';
import './Footer.css';

const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer-content">
                <p>&copy; {new Date().getFullYear()} IVEC. All rights reserved.</p>
                <p>Invest smart, grow your wealth.</p>
            </div>
        </footer>
    );
};

export default Footer;
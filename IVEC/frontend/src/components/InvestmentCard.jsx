import React from 'react';

const InvestmentCard = ({ investment }) => {
    const { title, capital, interestRate, currentValue, createdAt } = investment;

    return (
        <div className="investment-card">
            <h3>{title}</h3>
            <p>Capital: ${capital.toFixed(2)}</p>
            <p>Interest Rate: {interestRate}%</p>
            <p>Current Value: ${currentValue.toFixed(2)}</p>
            <p>Created At: {new Date(createdAt).toLocaleDateString()}</p>
        </div>
    );
};

export default InvestmentCard;
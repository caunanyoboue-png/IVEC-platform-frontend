import React, { useEffect, useState } from 'react';
import { fetchInvestments } from '../services/investmentService';
import InvestmentCard from '../components/InvestmentCard';

const Dashboard = () => {
    const [investments, setInvestments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const loadInvestments = async () => {
            try {
                const data = await fetchInvestments();
                setInvestments(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        loadInvestments();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div className="dashboard">
            <h1>Your Investments</h1>
            <div className="investment-list">
                {investments.map(investment => (
                    <InvestmentCard key={investment.id} investment={investment} />
                ))}
            </div>
        </div>
    );
};

export default Dashboard;
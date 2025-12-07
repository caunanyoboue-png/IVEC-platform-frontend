import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import investmentService from '../services/investmentService';

const InvestmentDetail = () => {
    const { id } = useParams();
    const [investment, setInvestment] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchInvestmentDetail = async () => {
            try {
                const response = await investmentService.getInvestmentById(id);
                setInvestment(response.data);
            } catch (err) {
                setError('Error fetching investment details');
            } finally {
                setLoading(false);
            }
        };

        fetchInvestmentDetail();
    }, [id]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div>
            <h1>Investment Detail</h1>
            {investment && (
                <div>
                    <h2>{investment.title}</h2>
                    <p>Capital: ${investment.capital}</p>
                    <p>Interest Rate: {investment.interest_rate}%</p>
                    <p>Current Value: ${investment.current_value}</p>
                    <p>Created At: {new Date(investment.created_at).toLocaleDateString()}</p>
                    <p>Last Updated: {new Date(investment.updated_at).toLocaleDateString()}</p>
                </div>
            )}
        </div>
    );
};

export default InvestmentDetail;
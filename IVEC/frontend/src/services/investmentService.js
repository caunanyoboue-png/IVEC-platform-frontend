import apiClient from '../api/apiClient';

const investmentService = {
    getInvestments: async () => {
        const response = await apiClient.get('/investments/');
        return response.data;
    },

    getInvestmentById: async (id) => {
        const response = await apiClient.get(`/investments/${id}/`);
        return response.data;
    },

    createInvestment: async (investmentData) => {
        const response = await apiClient.post('/investments/', investmentData);
        return response.data;
    },

    updateInvestment: async (id, investmentData) => {
        const response = await apiClient.put(`/investments/${id}/`, investmentData);
        return response.data;
    },

    deleteInvestment: async (id) => {
        await apiClient.delete(`/investments/${id}/`);
    },

    calculateInterest: async (id) => {
        const response = await apiClient.post(`/investments/${id}/calculate-interest/`);
        return response.data;
    }
};

export default investmentService;
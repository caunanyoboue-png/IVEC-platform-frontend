const API_URL = "http://127.0.0.1:8000/api/investments";

// 1. Récupérer le tableau de bord (Solde + Liste investissements)
export const fetchInvestments = async () => {
    const token = localStorage.getItem('access_token');
    
    const response = await fetch(`${API_URL}/dashboard/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });

    if (!response.ok) {
        throw new Error('Impossible de récupérer les données');
    }

    return await response.json();
};

// 2. Faire une demande de retrait
export const requestWithdrawal = async (amount) => {
    const token = localStorage.getItem('access_token');

    const response = await fetch(`${API_URL}/withdraw/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ amount })
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Erreur lors du retrait');
    }

    return await response.json();
};

// 3. Récupérer l'historique des transactions (C'est celle qui manquait !)
export const fetchTransactions = async () => {
    const token = localStorage.getItem('access_token');

    const response = await fetch(`${API_URL}/transactions/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });

    if (!response.ok) {
        throw new Error('Impossible de récupérer l\'historique');
    }

    return await response.json();
};

// Export par défaut pour les fichiers qui importent "tout" le service
const investmentService = {
    fetchInvestments,
    requestWithdrawal,
    fetchTransactions
};

export default investmentService;
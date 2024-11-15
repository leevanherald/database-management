// MainPage.js
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import DataProvision from './global/dataProvision/DataProvision';
import AnalyticsService from './global/analytics/AnalyticsService';
import Sidebar from './global/sidebar';
import Header from './global/Header';
import ExpressionEval from './global/expressionEval/ExpressionEval';
import PayrollCheck from './global/payrollCheck/PayrollCheck';
import Operations from './global/Operations/Operations';
import MotorAnalysisComponent from './global/motorAnalysis/MotorAnalysisComponent';
import TokenValidation from './global/components/TokenValidation'; // Token validation component

import ProtectedRoute from './global/components/ProtectedRoute';


const MainPage = () => {
  return (
    <BrowserRouter>
      <TokenValidation /> {/* Token Validation should happen here */}
      <div className="flex">
        <Header />
        <Sidebar />
        <div className="flex-grow">
          <Routes>
            <Route path="/data-provision" element={<ProtectedRoute element={<DataProvision />} />} />
            <Route path="/analytics" element={<ProtectedRoute element={<AnalyticsService />} />} />
            <Route path="/expression-eval" element={<ProtectedRoute element={<ExpressionEval />} />} />
            <Route path="/payroll-check" element={<ProtectedRoute element={<PayrollCheck />} />} />
            <Route path="/operations" element={<ProtectedRoute element={<Operations />} />} />
            <Route path="/motor-analysis" element={<ProtectedRoute element={<MotorAnalysisComponent />} />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default MainPage;

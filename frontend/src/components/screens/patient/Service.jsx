import React from 'react'

const Service = () => {
    
    const serviceType = [
        {ico: 'mdi mdi-arm-flex', name: 'Профилактические'},
        {ico: 'mdi mdi-account-tie', name: 'Экспертные'},
        {ico: 'mdi mdi-pill', name: 'Лечебные'},
        {ico: 'mdi mdi-chart-donut', name: 'Статистические'},
        {ico: 'mdi mdi-doctor', name: 'Консалтинговые'},
        {ico: 'mdi mdi-ambulance', name: 'Стационарные'},
        {ico: 'mdi mdi-dna', name: 'Диагностические'},
        {ico: 'mdi mdi-car-connected', name: 'Транспортные'},
    ]
    
    return (
        <div className='service__page'>
            <div className='service__type-wrap'>
                <div className='container'>
                    <div className='service__type-list'>
                        {serviceType.map(({ico, name}) => {
                            return <div key={Date.now()}><i className={ico}></i> <span>{name}</span></div>
                        })}
                    </div>
                    <div className='service__type-search'>
                        <i className='mdi mdi-robot-confused-outline'></i>
                        <div>
                            <div className='service__type-popular'>
                                <div><i className='mdi mdi-information-slab-circle-outline'></i> О сервисе</div>
                                <div><i className='mdi mdi-card-account-details-outline'></i> Медкарта</div>
                                <div><i className='mdi mdi-clipboard-list-outline'></i> Справочник</div>
                            </div>
                            <label className='service-type-search' htmlFor='search'>
                                <input id='search' name='search' type='text' inputMode='text' placeholder='Введите запрос' />
                                <i className='mdi mdi-magnify'></i>
                            </label>
                        </div>
                    </div>
                </div>
            </div>
            
            <div className='container'>
                <div className='page__section'>
                    <div className='page__section-title'>Популярные услуги</div>
                    <div className='page__section-content'>
                        
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Service
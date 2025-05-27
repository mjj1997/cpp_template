set(SRCS
    demo.cpp
)

message(STATUS "libs ${LIBS}")

if(BUILD_${PROJECT_NAME}_SHARED_LIBS)
    add_library(${PROJECT_NAME}_shared SHARED
        ${SRCS}
    )
    target_include_directories(${PROJECT_NAME}_shared PUBLIC
        ${PROJECT_SOURCE_DIR}/include
    )
    target_link_libraries(${PROJECT_NAME}_shared PRIVATE
        ${LIBS}
    )
    install(TARGETS ${PROJECT_NAME}_shared DESTINATION bin)
endif()

if(BUILD_${PROJECT_NAME}_STATIC_LIBS)
    add_library(${PROJECT_NAME}_static STATIC
        ${SRCS}
    )
    target_include_directories(${PROJECT_NAME}_static PUBLIC
        ${PROJECT_SOURCE_DIR}/include
    )
    target_link_libraries(${PROJECT_NAME}_static PRIVATE
        ${LIBS}
    )
    install(TARGETS ${PROJECT_NAME}_static DESTINATION lib)
endif()
